function [result, result_nodes] = SAHillClimb2(G, s, func)
% Input:  G - graph of the network
%         s - initial solution
%         func - function to use on the sets
    nNodes = numnodes(G);
    result_nodes = s;
    result = func(G, result_nodes);
    improved = true;
    while improved
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

