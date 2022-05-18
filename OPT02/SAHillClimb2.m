function [result, result_nodes] = SAHillClimb2(G, n, time, func)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         time - number of seconds to run the method
%         func - function to use on the sets
    t = tic;
    nNodes = numnodes(G);
    result_nodes = randperm(nNodes, n);
    result = func(G, result_nodes);
    improved = true;
    while toc(t) < time && improved
        D = [];
        r = inf;
        for a=result_nodes
            nnodes = setdiff(neighbors(G,a)', result_nodes);
            for b=nnodes
                tmp = [setdiff(result_nodes,a) b];
                tmpr = func(G, tmp);
                if tmpr < r
                    D = tmp;
                    r = tmpr;
                end
            end
        end
        if r < result
           result = r;
           result_nodes = D;
        else
            improved = false;
        end
    end
end

