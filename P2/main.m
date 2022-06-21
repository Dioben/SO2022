[Nodes,Links,L]= generateTopology(93391);
G = graph(L);

%% Show node graphs
if false
    figure(1);
    plotTopology(Nodes,Links,[]);
    figure(2);
    plotTopology(Nodes,Links,[16,26,30,33,40,66,73,92]);
    ConnectedNP(G,[16,26,30,33,40,66,73,92])
    figure(3);
    plotTopology(Nodes,Links,[16,26,28,33,40,48,57,61,69,73,86,97]);
    ConnectedNP(G,[16,26,28,33,40,48,57,61,69,73,86,97])
end

%% Generate lpt
if false
    exportToLP(size(Nodes,1),L,8,"critical8.lpt");
    exportToLP(size(Nodes,1),L,12,"critical12.lpt");
end

%% Grasp arg testing
if false
    results = [];
    for n=[8,12]
    for time=[1,30,60]
    for r=[1,2,3,4,5,6,7,8,9,10]
    results = [results; n time r GRASP(G,n,time,r,@ConnectedNP,@SAHillClimb1)];
    writematrix(results,"GRASP.csv");
    end
    end
    end
end

%% Memetic arg testing
if false
    results = [];
    for n=[8,12]
    for time=[1,30]
    for nPop=[5,10,15]
    for elitism=[1,2,3,4]
    for mutChance=[0,0.1,0.25,0.5,0.75,1]
    results = [results; n time nPop elitism mutChance Memetic(G,n,time,nPop,elitism,mutChance,@ConnectedNP,@SAHillClimb1) Memetic(G,n,time,nPop,elitism,mutChance,@ConnectedNP,@SAHillClimb2)];
    writematrix(results,"Memetic.csv");
    end
    end
    end
    end
    end
end

%% GRASP final results
if false
    results = [];
    for i=1:10
        results = [results; 8 GRASP(G,8,300,4,@ConnectedNP,@SAHillClimb1)];
        results = [results; 12 GRASP(G,12,300,8,@ConnectedNP,@SAHillClimb1)];
        writematrix(results,"GRASPFinal.csv");
    end
end

%% Memetic final results
if false
    results = [];
    for i=1:10
        t = tic();
        results = [results; 8 Memetic(G,8,300,15,2,0.75,@ConnectedNP,@SAHillClimb1) toc(t)];
        t = tic();
        results = [results; 12 Memetic(G,12,300,15,2,0.25,@ConnectedNP,@SAHillClimb1) toc(t)];
        writematrix(results,"MemeticFinal.csv");
    end
end

