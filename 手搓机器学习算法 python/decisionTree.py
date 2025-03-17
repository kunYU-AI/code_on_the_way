import numpy as np
from collections import Counter

# TreeNode
class TreeNode:
    '''
    Node:
    1. 特征相关量：split feature idx 当前节点的分裂特征索引，split threshold 分裂阈值
    2. 指针：左指针，右指针
    3. 特殊（叶子节点）：类别/预测值
    '''
    def __init__(self, feature_idx=None, threshold=None, left=None, right=None, value=None):
        self.feature_idx = feature_idx
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTree:
    '''
    methods:
        0. fit 
        1. _树的构建
        2. _最佳的分裂特征
        3. _最佳分裂点
        4. predict 预测/分类
    '''
    def __init__(self, max_depth=3, min_samples_split=2):
        '''
        树相关的量：
            1. 最大深度
            2. 节点的最小样本数（判断停止分裂）
            3. root node（但不需要提前设置）
        '''
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None
    
    def fit(self, X, y):
        '''
        模型训练的输入: train data, train label 
        模型的训练依赖的是: 
            1. Node的分裂: 想象从一个root依次分裂到一颗完整的树。
            2. 递归算法: 我们在TreeNode中，没有引入Node Level/Depth的记录量，
            所以需要在递归中引入
        '''
        self.root = self._grow_tree(X, y, depth) 
    
    # 递归建树
    def _grow_tree(self, X, y, depth):
        '''
        想象2维数据被特征划分成块，因此，数据集被划分为满足特征的子集(X,y)。
        我们在新的子集中，寻找最佳分裂特征和阈值。
        '''
        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))
        
        # 1.终止条件
        # 达到最大深度 or 纯度足够 or 样本数不足
        if (depth >= self.max_depth) or \
            (n_samples <= self.min_samples_split) or \
            (n_classes == 1):
            return TreeNode(value=self._most_common_label(y))
        
        # 2.分裂
        # 最佳分裂特征和阈值
        best_feature, best_threshold = self._best_split(X, y)
        # 分裂失败 = 所有数据的特征值相同. 返回叶子节点
        if best_feature is None:
            return TreeNode(value=self._most_common_label(y))
        
        # 3.根据最佳分裂点分割数据
        left_idxs = X[:, best_feature] <= best_threshold
        right_idxs = X[:, best_feature] > best_threshold
        left = self._grow_tree(X[left_idxs], y[left_idxs], depth+1)
        right = self._grow_tree(X[right_idxs], y[right_idxs], depth+1)

        return TreeNode(feature_idx=best_feature, threshold=best_threshold, left=left, right=right)
    
    # 寻找最佳分裂点: 
    # 在决策树中，基尼系数用于评估数据集的纯度，并指导节点分裂，
    # 目标是每次分裂都尽可能降低子节点的基尼系数，从而提高树的预测准确性。
    def _gini(self, y):
        counts = np.bincount(y)
        p = counts / len(y)
        return 1 - np.sum(p**2)

    def _best_split(self, X, y):
        '''
        步骤：
            1.计算当前节点的基尼系数
            2.(穷举所有)遍历所有可能的特征和分割点：连续特征一般考虑中位数；\
                离散特征一般考虑每个值
            3.计算每个分割点的基尼系数增益：得到子节点的基尼系数，加权平均
        '''
        best_gini = float('inf')
        best_feature, best_threshold = None, None 

        for feature_idx in range(X.shape[1]):
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                left_idxs = X[:, feature_idx] <= threshold
                right_idxs = X[:, feature_idx] > threshold

                if len(y[left_idxs]) == 0 or len(y[right_idxs]) == 0:
                    continue

                # 分裂后的加权基尼系数
                gini_left = self._gini(y[left_idxs])
                gini_right = self._gini(y[right_idxs])
                weighted_gini = (len(y[left_idxs])*gini_left + len(y[right_idxs])*gini_right) / len(y) 

                # 更新最佳分裂点和阈值
                if weighted_gini < best_gini:
                    best_gini = weighted_gini
                    best_feature = feature_idx
                    best_threshold = threshold
        return best_feature, best_threshold

    # 最大票数的标签
    def _most_common_label(self, y):
        counter = Counter(y)
        return counter.most_common(1)[0][0]

    # 预测样本
    def predict(self, X):
        return np.array([self._predict(x, self.root) for x in X])
    def _predict(self, x, node):
        # 我们只有子节点才储存了值
        if node.value is not None:
            return node.value
        if x[node.feature_idx] <= node.threshold:
            return self._predict(x, node.left)
        else:
            return self._predict(x, node.right)


# 示例：鸢尾花数据集分类
if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    # 加载数据
    iris = load_iris()
    X, y = iris.data, iris.target

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 训练模型
    tree = DecisionTreeClassifier(max_depth=3)
    tree.fit(X_train, y_train)

    # 预测并评估
    y_pred = tree.predict(X_test)
    print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
