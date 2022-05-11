function [result, result_nodes] = minlenNeighbor(G, best, time)
% Input:  G - graph of the network
%         best - current best set
%         time - number of seconds to run the method
    result = AverageSP(G,best);
    result_nodes = best;
    nNodes = numnodes(G);
    n = length(result_nodes);
    t = tic;
    while toc(t) < time
        others = setdiff(1:nNodes,result_nodes);
        neighbor = [result_nodes(randperm(n,n-1)) others(randperm(nNodes-n,1))];
        r = AverageSP(G,neighbor);
        if r < result
           result = r;
           result_nodes = neighbor;
        end
    end
end

