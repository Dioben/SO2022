function [result, result_nodes] = minlen(G, n, time)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         time - number of seconds to run the method
    result = inf;
    result_nodes = [];
    t = tic;
    nodes = numnodes(G);
    while toc(t) < time
        D = randperm(nodes, n);
        r = ConnectedNP(G, D);
        if r < result
           result = r;
           result_nodes = D;
        end
    end
end

