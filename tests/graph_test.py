import pytest
from mendola import graph
from nose.tools import assert_raises, assert_equal


def test_graph():
    net = graph.Graph()
    net.add_edge(0, 1, weight=5)
    net.add_edge(0, 5, weight=2)
    net.add_edge(1, 2, weight=3)
    net.add_edge(2, 3, weight=4)
    net.add_edge(3, 4, weight=5)
    net.add_edge(3, 5, weight=6)
    net.add_edge(4, 0, weight=7)
    net.add_edge(5, 4, weight=8)
    net.add_edge(5, 2, weight=9)

    assert_raises(TypeError, net.add_edge, None, 1)
    assert_raises(KeyError, net.add_edge, 5, 2, "1")
    assert_raises(TypeError, net.add_edge, 5, None)

    assert_equal(net.nodes[0].adj_weights[net.nodes[1].key], 5)
    assert_equal(net.nodes[0].adj_weights[net.nodes[5].key], 2)
    assert_equal(net.nodes[1].adj_weights[net.nodes[2].key], 3)
    assert_equal(net.nodes[2].adj_weights[net.nodes[3].key], 4)
    assert_equal(net.nodes[3].adj_weights[net.nodes[4].key], 5)
    assert_equal(net.nodes[3].adj_weights[net.nodes[5].key], 6)
    assert_equal(net.nodes[4].adj_weights[net.nodes[0].key], 7)
    assert_equal(net.nodes[5].adj_weights[net.nodes[4].key], 8)
    assert_equal(net.nodes[5].adj_weights[net.nodes[2].key], 9)

    assert_equal(net.nodes[0].incoming_edges, 1)
    assert_equal(net.nodes[1].incoming_edges, 1)
    assert_equal(net.nodes[2].incoming_edges, 2)
    assert_equal(net.nodes[3].incoming_edges, 1)
    assert_equal(net.nodes[4].incoming_edges, 2)
    assert_equal(net.nodes[5].incoming_edges, 2)

    assert_equal(len(net.nodes[0].adj_nodes), 2)
    assert_equal(len(net.nodes[1].adj_nodes), 1)
    assert_equal(len(net.nodes[2].adj_nodes), 1)
    assert_equal(len(net.nodes[3].adj_nodes), 2)
    assert_equal(len(net.nodes[4].adj_nodes), 1)
    assert_equal(len(net.nodes[5].adj_nodes), 2)

    net.nodes[0].remove_neighbor(net.nodes[1])
    assert_equal(net.nodes[1].incoming_edges, 0)
    net.nodes[3].remove_neighbor(net.nodes[4])
    assert_equal(net.nodes[4].incoming_edges, 1)

    assert_equal(net.nodes[0] < net.nodes[1], True)


if __name__ == '__main__':
    pytest.main([__file__])
