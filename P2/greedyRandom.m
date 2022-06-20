function [final_nodes] = greedyRandom(G,n,r,ResFunc)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         r - number of best next nodes to decide from
%         ResFunc - function to calculate a result from a set
    unusedNodes = 1:numnodes(G);
    final_nodes = [];
    for i = 1:n
        nodeSet = [];
        for node = unusedNodes
            nodeSet = [nodeSet ; node ResFunc(G,[final_nodes node])];
        end
        nodeSet = sortrows(nodeSet,2);
        newNode = nodeSet(randi(r),1);
        final_nodes = [final_nodes newNode];
        unusedNodes = setdiff(unusedNodes,newNode);
    end
end

