function [final_result,final_nodes] = SAHillClimb2(G,s,ResFunc)
% Input:  G - graph of the network
%         s - initial solution
%         ResFunc - function to calculate a result from a set
    final_nodes = s;
    final_result = ResFunc(G,final_nodes);
    improved = true;
    while improved
        result = inf;
        for oldNode=final_nodes
            neighborNodes = setdiff(neighbors(G,oldNode)',final_nodes);
            for newNode=neighborNodes
                tmpNodes = [setdiff(final_nodes,oldNode) newNode];
                tmpResult = ResFunc(G,tmpNodes);
                if tmpResult < result
                    nodes = tmpNodes;
                    result = tmpResult;
                end
            end
        end
        if result < final_result
            final_result = result;
            final_nodes = nodes;
        else
            improved = false;
        end
    end
end

