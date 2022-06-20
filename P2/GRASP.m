function [final_result,final_nodes] = GRASP(G,n,time,r,ResFunc,LocalSearch)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         time - number of seconds to run this method
%         r - number of best next nodes to decide from in the random greedy
%         ResFunc - function to calculate a result from a set
%         LocalSearch - function that finds the closest local minimum
    t = tic();
    nodes = greedyRandom(G,n,r,ResFunc);
    [final_result,final_nodes] = LocalSearch(G,nodes,ResFunc);
    while toc(t) < time
        nodes = greedyRandom(G,n,r,ResFunc);
        [result,nodes] = LocalSearch(G,nodes,ResFunc);
        if result < final_result
            final_result = result;
            final_nodes = nodes;
        end
    end
end

