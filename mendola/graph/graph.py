# -*- coding: UTF-8 -*-
from __future__ import print_function
from enum import Enum


class State(Enum):
    unvisited = 0
    visiting = 1
    visited = 2


class Node:
    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        if neighbor is None or not isinstance(weight, (int, long, float)):
            raise TypeError('neighbor or weight must be numerical')
        neighbor.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError('neighbor cannot be None')
        if neighbor.key not in self.adj_nodes:
            raise KeyError('neighbor not found')
        neighbor.incoming_edges -= 1
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]


class Graph:
    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def _add_node(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, src_key, dst_key, weight=0):
        if src_key is None or dst_key is None:
            raise TypeError('key cannot be None')
        if not isinstance(weight, (int, long, float)):
            raise KeyError('weight must be numerical')
        if src_key not in self.nodes:
            self._add_node(src_key)
        if dst_key not in self.nodes:
            self._add_node(dst_key)
        self.nodes[src_key].add_neighbor(self.nodes[dst_key], weight)

    def add_undirected_edge(self, src_key, dst_key, weight=0):
        if src_key is None or dst_key is None:
            raise TypeError('key cannot be None')
        if not isinstance(weight, (int, long, float)):
            raise KeyError('weight must be numerical')
        self.add_edge(src_key, dst_key, weight)
        self.add_edge(dst_key, src_key, weight)
