Nodes = load("Nodes.txt");
Links = load("Links.txt");
L = load("L.txt");
nNodes = size(Nodes, 1);
nLinks = size(Links, 1);
G = graph(L);

figure(1);

plotTopology(Nodes, Links,[]);

[res, nodes] = minlen(G,8,30)

[res_2, nodes_2] = split(G,8,30)

