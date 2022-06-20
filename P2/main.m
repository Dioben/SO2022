[Nodes,Links,L]= generateTopology(93391);
G = graph(L);

% figure(1);
% plotTopology(Nodes,Links,[]);

% exportToLP(size(Nodes,1),L,8,"critical8.lpt");

results = [];
for n=[8,12]
for time=[5,10,20]
for r=[1,2,3,4,5,10]
results = [results; n time r GRASP(G,n,time,r,@ConnectedNP,@SAHillClimb1) GRASP(G,n,time,r,@ConnectedNP,@SAHillClimb2)];
writematrix(results,"GRASP.csv");
end
end
end

results = [];
for n=[8,12]
for time=[5,10,20]
for nPop=[5,10,20,30]
for elitism=[1,2,3,4]
for mutChance=[0,0.25,0.5,0.75,1]
if nPop>elitism
results = [results; n time nPop elitism mutChance Memetic(G,n,time,nPop,elitism,mutChance,@ConnectedNP,@SAHillClimb1) Memetic(G,n,time,nPop,elitism,mutChance,@ConnectedNP,@SAHillClimb2)];
writematrix(results,"Memetic.csv");
end
end
end
end
end
end