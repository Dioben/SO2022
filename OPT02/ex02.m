Nodes = load("Nodes2.txt");
Links = load("Links2.txt");
L = load("L2.txt");
nNodes = size(Nodes, 1);
nLinks = size(Links, 1);
G = graph(L);

[res, nodes] = SAHillClimb1(G, 10, 30, @AverageSP)

[res2, nodes2] = SAHillClimb2(G, 10, 30, @AverageSP)

