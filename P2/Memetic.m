function [final_result,final_nodes] = Memetic(G,n,time,nPop,elitism,mutChance,ResFunc,LocalSearch)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         time - number of seconds to run this method
%         nPop - number of elements in the population
%         elitism - how many of the best individuals are garanteed to survive
%         mutChance - mutation chance
%         ResFunc - function to calculate a result from a set
%         LocalSearch - function that finds the closest local minimum
    t = tic();
    nNodes = numnodes(G);
    population = [];
    for i=1:nPop
        individual = randperm(nNodes, n);
        [result, nodes] = LocalSearch(G,individual,ResFunc);
        population = [population; result nodes];
    end
    while toc(t) < time
        nextPopulation = [];
        for i=1:nPop
            child = Crossover(population,G,ResFunc);
            if rand(1,1) < mutChance
                child = Mutation(child,nNodes,G,ResFunc);
            end
            child(:,1) = [];
            [result, nodes] = LocalSearch(G,child,ResFunc);
            nextPopulation = [nextPopulation ; result nodes];
        end
        population = Selection(population,nextPopulation,elitism);
    end
    best = sortrows(population);
    final_result = best(1,1);
    final_nodes = best(1,2:size(best,2)-1);
end

function [child] = Crossover(population,G,ResFunc)
    individual1 = population(randi(size(population,1)),:);
    P = setdiff(population,individual1,'rows');
    individual2 = P(randi(size(P,1)),:);
    if individual1(1) < individual2(1)
        parent1 = individual1;
    else
        parent1 = individual2;
    end
    P = setdiff(population,parent1,'rows');
    individual1 = P(randi(size(P,1)),:);
    P = setdiff(population,[parent1 ; individual1],'rows');
    individual2 = P(randi(size(P,1)),:);
    if individual1(1) < individual2(1)
        parent2 = individual1;
    else
        parent2 = individual2;
    end
    parent1(:,1) = [];
    parent2(:,1) = [];
    child = union(parent1,parent2);
    child = child(:,randperm(length(child),length(parent1)));
    child = [ResFunc(G,child) child];
end

function [individual] = Mutation(individual,nNodes,G,ResFunc)
    individual(:,1) = [];
    indLength = length(individual);
    otherNodes = setdiff(1:nNodes,individual);
    individual = individual(:,randperm(indLength,randi(indLength-1)));
    otherNodes = otherNodes(:,randperm(length(otherNodes),indLength-length(individual)));
    individual = [individual otherNodes];
    individual = [ResFunc(G,individual) individual];
end

function [P] = Selection(population,nextPopulation,elitism)
    P = sortrows(union(population,nextPopulation,'rows'));
    elites = P(1:elitism,:);
    P(1,:) = [];
    P = [elites ; P(randperm(size(P,1),size(population,1)-elitism),:)];
end