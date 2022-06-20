function [Nodes,Links,L]= generateTopology(num)

    nNodes= 100;
    dimX= 100;
    dimY= 100;
    diferenca= 4;
 
    Nodes= zeros(nNodes,2);
    i= 0;
    rng(num);
    while i < nNodes
        new= [rand()*dimX rand()*dimY];
        sim= true;
        for j= 1:i-1
            if sqrt((Nodes(j,1)-new(1))^2+(Nodes(j,2)-new(2))^2) <= diferenca
                sim= false;
                break;
            end
        end
        if sim
            i= i+1;
            Nodes(i,:)= new;
        end
    end
    Nodes= sortrows(Nodes,[2 1]);
    Links= [];

    Ltotal= inf(nNodes);
    for i= 1:nNodes-1
        for j= i+1:nNodes
            aux= sqrt((Nodes(i,1)-Nodes(j,1))^2+(Nodes(i,2)-Nodes(j,2))^2);
            Ltotal(i,j)= aux;
            Ltotal(j,i)= aux;
        end
    end
    contador= 0;
    for i = 1:nNodes-1
        for j= i+1:nNodes
            kt= setdiff(1:nNodes,[i j]);
            sim= true;
            for k = kt
                if (Ltotal(i,j) > Ltotal(i,k)) && (Ltotal(i,j) > Ltotal(k,j))
                    sim= false;
                    break
                end
            end
            if sim
                contador= contador + 1;
                Links(contador,:) = [i j];
            end
        end
    end
    L= zeros(nNodes);
    for i= 1:size(Links,1)
        L(Links(i,1),Links(i,2))= Ltotal(Links(i,1),Links(i,2));
        L(Links(i,2),Links(i,1))= Ltotal(Links(i,1),Links(i,2));
    end
end
