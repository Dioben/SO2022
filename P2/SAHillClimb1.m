function [final_result,final_nodes] = SAHillClimb1(G,s,ResFunc)
% Input:  G - graph of the network
%         s - initial solution
%         ResFunc - function to calculate a result from a set
    nNodes = numnodes(G);
    final_nodes = s;
    final_result = ResFunc(G,final_nodes);
    improved = true;
    while improved
        result = final_result;
        unusedNodes = setdiff(1:nNodes,final_nodes);
        for oldNode=final_nodes
            for newNode=unusedNodes
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

