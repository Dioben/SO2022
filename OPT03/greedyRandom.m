function [result,result_nodes] = greedyRandom(G,n,r,func)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         r - number of best next nodes to decide from
%         func - function to use on the sets
    E = 1:numnodes(G);
    result_nodes = [];
    for i = 1:n
        R = [];
        for j = E
            R = [R ; j func(G,[result_nodes j])];
        end
        R = sortrows(R,2);
        e = R(randi(r),1);
        result_nodes = [result_nodes e];
        E = setdiff(E,e);
    end
    result = func(G,result_nodes);
end

