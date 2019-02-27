#!/usr/bin/env python3

import re
import itertools

ROLLNUM_REGEX = "201[0-9]{4}"

class Graph(object):
    name = "Amandeep Kaur"
    email = "amandeep18014@iiitd.ac.in"
    roll_num = "2018014"

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges    = ordered_edges
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

    def create(self,vertices,edges):
    	g={}
    	for i in vertices:
    		g[i]=[]
    		for j in edges:
    			if i==j[0]:
    				g[i].append(j[1])
    			elif i==j[1]:
    				g[i].append(j[0])
    	return(g)

    def all_paths(self,start_node,end_node,path=''):
    	'''Takes in start note and end note

    	Returns:returns all paths between start node and end node
    	'''
    	g=graph.create(vertices,edges)
    	path+=str(start_node)
    	if start_node==end_node:
    		return [path]     
    	paths=[]
    	for i in g[start_node]:
    		if str(i) in path:
    			pass
    		else:
    			new_p=self.all_paths(i,end_node,path)
    			for j in new_p:
    				paths.append(j)
    	return paths


    def min_dist(self, start_node, end_node):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from
            end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
        lst=graph.all_paths(start_node,end_node)
        trash={}
        for i in lst:
        	trash[len(i)]=i
        ans=min(list(trash.keys()))
        return ans
        raise NotImplementedError

    def all_shortest_paths(self,start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """
        lst=graph.all_paths(start_node,end_node)
        trash={}
        for i in lst:
        	if len(i) in trash:
        		trash[len(i)].append(i)
        	else:
        		trash[len(i)]=[i]
        ans=min(list(trash.keys()))
        req=[]
        for i in trash:
        	if i==ans:
        		for j in range(len(trash[i])):
        			req.append(trash[i][j])
        return req
        raise NotImplementedError


    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
        pairs=[]
        for i in vertices:
        	for j in vertices:
        		if i!=j and (i,j)[::-1] not in pairs and i!=node and j!=node:
        			pairs.append((i,j))
        sp_node_pair=[]
        sp_through_node=[]
        for i in pairs:
        	a=0
        	s,e=list(i)
        	ap=graph.all_shortest_paths(s,e)
        	sp_node_pair.append(len(ap))
        	for i in ap:
        		if str(node) in i:
        			a+=1
        	sp_through_node.append(a)
        bc_per_pair=[]
        for i in range(len(sp_node_pair)):
        	for j in range(len(sp_through_node)):
        		if i==j:
        			bc_per_pair.append(sp_through_node[j]/sp_node_pair[i])
        ans=0
        for i in bc_per_pair:
        	ans+=i
        return ans
        raise NotImplementedError

    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.
        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """
        bc_per_vertice={}
        for i in vertices:
        	bc_per_vertice[i]=graph.betweenness_centrality(i)
        ans=max(bc_per_vertice.values())
        req=[]
        for i in bc_per_vertice:
        	if bc_per_vertice[i]==ans:
        		req.append(i)
        return req
        raise NotImplementedError

if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6]
    edges    = [(1,2),(1,5),(2,3),(2,5),(3,4),(4,5),(4,6)]
    graph = Graph(vertices, edges)
    print(graph.top_k_betweenness_centrality())
