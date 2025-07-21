hold on
rsrp_avg = movmean(graphMatFile(1,:),500);
rsrp_avg = rsrp_avg*1.244 + 145.64;
% plot(rsrp_avg)

rsrp_avg_rj = movmean(averageRSRP_list(1,:),500);
rsrp_avg_rj = rsrp_avg_rj*1.244 + 145.64;
% plot(rsrp_avg_rj)

rsrp_avg_ES = movmean(averageRSRP_ES(1,:),500);
rsrp_avg_ES = rsrp_avg_ES*1.244 + 145.64;
% plot(rsrp_avg_ES)

%%
figure();
set(gca,'FontSize',42,'FontName','Times New Roman');
hold on
xlabel('Episode index','FontSize',42,'FontName','Times New Roman');
xlim([0 40000])
ylabel('Throughput (Mbps)','FontSize',42,'FontName','Times New Roman');

hold on
plot(rsrp_avg,'LineWidth',2.5);
plot(rsrp_avg_ES,'LineWidth',2.5);
plot(rsrp_avg_rj,'LineWidth',2.5)
legend('ASCEND','Reward-based ES','Random Jump','FontName','Times New Roman');