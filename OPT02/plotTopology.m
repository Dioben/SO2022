function plotTopology(Nodes,Links,servers)
% plotTopology(Nodes,Links,servers) - plots the network topology with servers in red
%
% Nodes:   a matrix with 2 columns with the (x,y) coordinates of each node
% Links:   a matrix with 2 columns with the end nodes of each link
% servers: a row array of server nodes (can be an empty row)

    nNodes= size(Nodes,1);
    %plot the links:
    plot([Nodes(Links(1,1),1) Nodes(Links(1,2),1)],[Nodes(Links(1,1),2) Nodes(Links(1,2),2)],'k-');
    hold on
    for i=2:size(Links,1)
        plot([Nodes(Links(i,1),1) Nodes(Links(i,2),1)],[Nodes(Links(i,1),2) Nodes(Links(i,2),2)],'k-')
    end
    clients= setdiff(1:nNodes,servers);
    %plot the non-server nodes:
    plot(Nodes(clients,1),Nodes(clients,2),'o','MarkerEdgeColor','k','MarkerFaceColor','w','MarkerSize',10)
    for i=clients
        text(Nodes(i,1),Nodes(i,2),sprintf('%d',i),'HorizontalAlignment','center','Color','k','FontSize',6);
    end
    % plot the server nodes:
    plot(Nodes(servers,1),Nodes(servers,2),'o','MarkerEdgeColor','r','MarkerFaceColor','w','MarkerSize',10)
    for i=servers
        text(Nodes(i,1),Nodes(i,2),sprintf('%d',i),'HorizontalAlignment','center','Color','r','FontSize',6);
    end    
    grid on
    hold off
end