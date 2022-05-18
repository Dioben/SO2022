function [result, result_nodes] = SimulatedAnnealing(G, n, time, func, iperc, fperc)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         time - number of seconds to run the method
%         func - function to use on the sets
%         iperc - initial percentage
%         fperc - final percentage wanted
    decT = @(curr_res, tc) -curr_res/log(tc/time * (iperc-fperc) + fperc); % linear decrease in percentage along time
    t = tic;
    nNodes = numnodes(G);
    result_nodes = randperm(nNodes, n);
    result = func(G, result_nodes);
    curr_nodes = result_nodes;
    curr_res = result;
    T = -curr_res/log(iperc);
    while toc(t) < time
        tc = toc(t);
        i = curr_nodes(randperm(n,1));
        nnodes = setdiff(neighbors(G,i)', curr_nodes);
        if isempty(nnodes)
            continue
        end
        D = [setdiff(curr_nodes, i) nnodes(randperm(length(nnodes),1))];
        r = func(G, D);
        if r < curr_res
            curr_nodes = D;
            curr_res = r;
            if curr_res < result
                result_nodes = curr_nodes;
                result = curr_res;
            end
        else
            if rand(1,1) < exp(1)^((curr_res-r)/T)
                curr_nodes = D;
                curr_res = r;
            end
        end
        T = decT(curr_res, tc);
    end
end

