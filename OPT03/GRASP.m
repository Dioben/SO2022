function [result,result_nodes] = GRASP(G,n,time,rn,func,HCfunc)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         time - number of seconds to run this method
%         rn - number of best next nodes to decide from in the random greedy
%         func - function to use on the sets
%         HCfunc - hill climbing function to use
    t = tic();
    [~,s] = greedyRandom(G,n,rn,func);
    [result,result_nodes] = HCfunc(G,s,func);
    while toc(t) < time
        [~,s] = greedyRandom(G,n,rn,func);
        [r,s] = HCfunc(G,s,func);
        if r < result
            result = r;
            result_nodes = s;
        end
    end
end

