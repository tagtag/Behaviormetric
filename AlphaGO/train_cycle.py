# ====================
# 学習サイクルの実行
# ====================

# パッケージのインポート
from dual_network import dual_network
from self_play import self_play
from train_network import train_network
from evaluate_network import evaluate_network
from evaluate_best_player import evaluate_best_player

# デュアルネットワークの作成
dual_network()

for i in range(10):
    print('Train',i,'====================')
    # セルフプレイ部
    self_play()

    # パラメータ更新部
    train_network()

    # 新パラメータ評価部
    update_best_player = evaluate_network()

    # ベストプレイヤーの評価
    if update_best_player:
        evaluate_best_player()