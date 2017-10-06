# pylint: disable=missing-docstring, global-statement, invalid-name, too-few-public-methods
#
# Copyright (C) 2017  Jonas Colmsjö, Claes Strannegård
#


# Imports
# ======

import unittest
from gzutils.gzutils import Logging
from ecosystem.network import Network, MotorNetwork


# Setup logging
# =============

DEBUG_MODE = True
l = Logging('test_network', DEBUG_MODE)


class Thing1:
    pass

class Thing2:
    pass

class Thing3:
    pass

class TestNetwork(unittest.TestCase):

    def setUp(self):
        l.info('Testing network...')

    def tearDown(self):
        l.info('...done with test_network.')

    def test_SENSOR_AND(self):
        network = Network()
        network.add_SENSOR_node(Thing1)

        self.assertTrue(network.getT() == (None,))

        network.update([(Thing2(), 1.0)])
        self.assertTrue(network.getT() == (False,))

        network.update([(Thing1(), 1.0)])
        self.assertTrue(network.getT() == (True,))

        network.add_SENSOR_node(Thing2)
        network.update([(Thing2(), 1.0)])
        self.assertTrue(network.getT() == (False, True, ))

        network.update([])
        self.assertTrue(network.getT() == (False, False, ))

        network.update([(Thing2(), 2.0), (Thing1(), 0.5)])
        self.assertTrue(network.getT() == (True, True, ))

        network.add_AND_node([0, 1])
        network.update([(Thing2(), 1.0), (Thing1(), 0.3)])
        self.assertTrue(network.getT() == (True, True, True))

        network.update([(Thing2(), 2.0)])
        self.assertTrue(network.getT() == (False, True, False))

    def test_SEQ(self):
        network = Network([('thing1', Thing1), ('thing2', Thing2)])
        network.add_SEQ_node([0, 1])

        network.update([(Thing1(), 1.0)])
        self.assertTrue(network.getT() == (True, False, False))

        network.update([(Thing2(), 0.5)])
        self.assertTrue(network.getT() == (False, True, True))

        network.update([(Thing2(), 1.0)])
        self.assertTrue(network.getT() == (False, True, False))

        network.update([])
        self.assertTrue(network.getT() == (False, False, False))


    def test_top_active(self):
        network = Network()
        n1 = network.add_SENSOR_node(Thing1)
        n2 = network.add_SENSOR_node(Thing2)
        n3 = network.add_SENSOR_node(Thing3)
        n4 = network.add_SEQ_node([n1, n2, n3])

        network.update([(Thing1(), 1.0)])
        self.assertTrue(network.get() == set([n1]))
        self.assertTrue(network.top_active() == set([n1]))

        network.update([(Thing2(), 1.0)])
        self.assertTrue(network.get() == set([n2]))
        self.assertTrue(network.top_active() == set([n2]))

        network.update([(Thing3(), 1.0)])
        self.assertTrue(network.get() == set([n3, n4]))
        self.assertTrue(network.top_active() == set([n4]))

        network.update([])
        self.assertTrue(network.get() == set())

        # Check that SEQ can keep track of multiple sequences at the same time
        network.update([(Thing1(), 1.0)])
        network.update([(Thing2(), 1.0), (Thing1(), 1.0)])
        network.update([(Thing3(), 1.0), (Thing2(), 1.0)])
        self.assertTrue(network.get() == set([n3, n2, n4]))
        network.update([(Thing3(), 1.0)])
        self.assertTrue(network.get() == set([n3, n4]))



class TestMotorNetwork(unittest.TestCase):

    def setUp(self):
        l.info('Testing MotorNetwork...')

    def tearDown(self):
        l.info('...done with MotorNetwork.')

    def test_MOTOR_AND_SEQ(self):
        mnetwork = MotorNetwork()
        n1 = mnetwork.add_MOTOR_node('m1')
        self.assertTrue(mnetwork.get() == set())

        mnetwork.update(set([n1]))
        self.assertTrue(mnetwork.get() == set([0]))

        mnetwork.update(set())
        self.assertTrue(mnetwork.get() == set())

        n2 = mnetwork.add_MOTOR_node('m2')
        mnetwork.update(set([n2]))
        self.assertTrue(mnetwork.get() == set([n2]))

        mnetwork.update(set([n2, n1]))
        self.assertTrue(mnetwork.get() == set([n1, n2]))

        n3 = mnetwork.add_MAND_node([n1, n2])
        mnetwork.update(set())
        self.assertTrue(mnetwork.get() == set())
        mnetwork.update(set([n3]))
        self.assertTrue(mnetwork.get() == set([n1, n2]))

        n4 = mnetwork.add_MOTOR_node('m3')
        n5 = mnetwork.add_MSEQ_node([n3, n4])
        mnetwork.update(set())
        self.assertTrue(mnetwork.get() == set())
        mnetwork.update(set())
        self.assertTrue(mnetwork.get() == set())
        mnetwork.update(set([n5]))
        self.assertTrue(mnetwork.get() == set([n1, n2]))
        mnetwork.update(set())
        self.assertTrue(mnetwork.get() == set([n4]))
        mnetwork.update(set())
        self.assertTrue(mnetwork.get() == set())

        mnetwork.delete_nodes([n5])
        mnetwork.update(set([n4]))
        self.assertTrue(mnetwork.get() == set([n4]))
