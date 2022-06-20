[Nodes,Links,L]= generateTopology(93391);
G = graph(L);

% figure(1);
% plotTopology(Nodes,Links,[]);

[graspRes,graspNodes]= GRASP(G,8,30,4,@ConnectedNP,@SAHillClimb1)
[memRes,memNodes]= Memetic(G,8,30,10,1,0.1,@ConnectedNP,@SAHillClimb2)
% exportToLP(size(Nodes,1),L,8,"critical8.lpt");
% greedyRandom(G,8,1,@ConnectedNP)