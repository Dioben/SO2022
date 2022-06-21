[Nodes,Links,L]= generateTopology(93391);
G = graph(L);

% figure(1);
% plotTopology(Nodes,Links,[]);

% exportToLP(size(Nodes,1),L,8,"critical8.lpt");
% exportToLP(size(Nodes,1),L,12,"critical12.lpt");

% results = [];
% for n=[8,12]
% for time=[1,30,60]
% for r=[1,2,3,4,5,6,7,8,9,10]
% results = [results; n time r GRASP(G,n,time,r,@ConnectedNP,@SAHillClimb1)];
% writematrix(results,"GRASP.csv");
% end
% end
% end

% results = [];
% for n=[8,12]
% for time=[1,30]
% for nPop=[5,10,15]
% for elitism=[1,2,3,4]
% for mutChance=[0,0.1,0.25,0.5,0.75,1]
% results = [results; n time nPop elitism mutChance Memetic(G,n,time,nPop,elitism,mutChance,@ConnectedNP,@SAHillClimb1) Memetic(G,n,time,nPop,elitism,mutChance,@ConnectedNP,@SAHillClimb2)];
% writematrix(results,"Memetic.csv");
% end
% end
% end
% end
% end

