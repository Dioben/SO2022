function [result,result_nodes] = Memetic(G,n,time,pop,elit,mut,func,HCfunc)
% Input:  G - graph of the network
%         n - number of nodes of set S
%         time - number of seconds to run this method
%         pop - number of elements in the population
%         elit - elitism
%         mut - mutation chance
%         func - function to use on the sets
%         HCfunc - hill climbing function to use
    t = tic();
    nNodes = numnodes(G);
    P = [];
    for i=1:pop
        x = randperm(nNodes, n);
        % P = [P ; HCfunc(G,x,func)];
        P = [P; func(G,x) x];
    end
    while toc(t) < time
        P2 = [];
        for i=1:pop
            x = Crossover(P,G,func);
            if rand(1,1) < mut
                x = Mutation(x,nNodes,G,func);
            end
            x(:,1) = [];
            [r, r2] = HCfunc(G,x,func);
            P2 = [P2 ; r r2];
        end
        P = Selection(P,P2,elit);
    end
    best = sortrows(P);
    result = best(1,1);
    result_nodes = best(2,length(best)-1);
end

function [child] = Crossover(P,G,func)
    x1 = P(randi(size(P,1)),:);
    P2 = setdiff(P,x1,'rows');
    x2 = P2(randi(size(P2,1)),:);
    if x1(1) < x2(1)
        p1 = x1;
    else
        p1 = x2;
    end
    P2 = setdiff(P,p1,'rows');
    x1 = P2(randi(size(P2,1)),:);
    P2 = setdiff(P,[p1 ; x1],'rows');
    x2 = P2(randi(size(P2,1)),:);
    if x1(1) < x2(1)
        p2 = x1;
    else
        p2 = x2;
    end
    p1(:,1) = [];
    p2(:,1) = [];
    child = union(p1,p2);
    child = child(:,randperm(length(child),length(p1)));
    child = [func(G,child) child];
end

function [x] = Mutation(x,nNodes,G,func)
    x(:,1) = [];
    x = x(:,randperm(length(x),length(x)-1));
    y = setdiff(1:nNodes,x);
    y = y(:,randperm(length(y),1));
    x = [x y];
    x = [func(G,x) x];
end

function [P3] = Selection(P,P2,elit)
    P
    P2
    P3 = sortrows([P P2])
    elits = P3(1,elit);
    P3 = [elits randperm(setdiff(P3,elits),length(P)-elit)];
end