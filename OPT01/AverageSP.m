function out=AverageSP(G,servers)
% AverageSP(G,servers) - Computes the average shortest path length from
%           each node to its closest server (returns -1 for invalid input data)
%
% G:       graph of the network
% servers: a row array of server nodes
    
    nNodes= numnodes(G);
    if length(servers)<1
        out= -1;
        return
    end
    if (max(servers)>nNodes || min(servers)<1 || length(unique(servers))<length(servers))
        out= -1;
        return
    end
    clients= setdiff(1:nNodes,servers);
    dist= distances(G,servers,clients);
    if length(servers)>1
        out= sum(min(dist))/nNodes;
    else
        out= sum(dist)/nNodes;
    end
end