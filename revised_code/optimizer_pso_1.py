import numpy as np
import matplotlib.pyplot as plt
import math
import time
from system6_fitness import get_fitness


class Swarm:
    def __init__(self, population, dimension):
        """
        :param population: 种群数量
        :param dimension: 维度
        """
        self.population = population  # 种群数量
        self.dimension = dimension  # 搜索维度
        self.position = np.zeros((self.population, self.dimension))  # 所有个体的位置
        self.velocity = np.zeros((self.population, self.dimension))  # 所有个体的速度
        self.pbest = np.zeros((self.population, self.dimension))  # 所有个体经历的最佳位置
        self.gbest = np.zeros((1, self.dimension))  # 全局最佳位置
        self.best_fitness = np.zeros((self.population, 1))  # 所有个体的历史最佳适应值
        self.search_domain_down = np.zeros_like(self.position)  # 搜索空间下限
        self.search_domain_up = np.zeros_like(self.position)  # 搜索空间上限
        self.global_best_fitness_history = [] # 历代全局最优适应值

    # 初始化群体
    def swarm_init(self, search_domain):
        """
        :param search_domain: list, 问题阈、搜索空间
        :return:
        """
        print("Initialize population...")
        self.search_domain_down = np.ones_like(self.position)*search_domain[0]
        self.search_domain_up = np.ones_like(self.position) * search_domain[1]

        self.position = np.random.uniform(search_domain[0], search_domain[1],
                                          [self.population, self.dimension])  # 初始化种群位置
        self.velocity = np.random.uniform(search_domain[0], search_domain[1],
                                          [self.population, self.dimension])  # 初始化种群速度
        # 个性化调整——偶数列搜索空间*2pi
        for i in range(0, np.size(self.position, 0)):
            self.position[i] = [x * 2 * math.pi if i % 2 == 1 else x for i, x in enumerate(self.position[i])]
            self.velocity[i] = [x * 2 * math.pi if i % 2 == 1 else x for i, x in enumerate(self.velocity[i])]
            self.search_domain_up[i] = [x * 2 * math.pi if i % 2 == 1 else x for i, x in enumerate(self.search_domain_up[i])]

        self.pbest = self.position  # 种群个体最优位置
        self.best_fitness = get_fitness(self.position)  # 计算适应值
        min_index = np.unravel_index(np.argmin(self.best_fitness, axis=None), self.best_fitness.shape)  # 获取最小适应度位置
        self.gbest = self.pbest[min_index]  # 获得全局最优个体

    # 调整位置
    def adjustP(self, position):
        """
        :param position: 个体位置
        :return:
        """
        flag = position > self.search_domain_up
        position = position * ~flag + (position - self.search_domain_up) * flag
        flag = position < self.search_domain_down
        position = position * ~flag + (self.search_domain_down - position) * flag
        return position

    # 调整位置
    def adjustV(self, velocity):
        """
        :param velocity: 个体速度
        :return:
        """
        sign = np.where(velocity>0, 1, -1)
        flag = np.abs(velocity) > self.search_domain_up*0.5
        velocity = (np.abs(velocity) * ~flag + self.search_domain_up*0.5 * flag) * sign
        return velocity


    # 训练
    def train(self, w, c1, c2, max_iter):
        """
        :param w: 惯性权重
        :param c1: 认知系数
        :param c2: 社会系数
        :param max_iter: 最大迭代次数
        :return:
        """
        current_v = self.velocity
        current_p = self.position
        # 迭代训练
        for i in range(max_iter):
            print(f"The {i+1}-th round of training...")
            # 更新位置和速度
            # 对应公式 vi+1 = w * vi + c1 * rand1 * (pbesti - xi) + c2 * rand2 * (gbest - xi)
            #         xi+1 = xi + vi+1
            w = w - (i - 1) * 0.02 / (max_iter - 1)  # 权重线性递减
            current_v = w*current_v + c1*np.random.random([self.population, self.dimension])*(self.pbest - current_p) +\
                        c2*np.random.random([self.population, self.dimension])*(self.gbest - current_p)  # 更新速度
            current_v = self.adjustV(current_v)
            current_p = current_v + current_p  # 更新位置
            current_p = self.adjustP(current_p)  # 调整位置
            current_fitness = get_fitness(current_p)  # 计算适应值

            # 更新种群个体的历史最优值
            flag = current_fitness < self.best_fitness
            self.pbest = np.multiply(flag, current_p.T).T + np.multiply(~flag, self.pbest.T).T

            # 更新群体历史最优个体
            self.best_fitness = np.minimum(current_fitness, self.best_fitness)  # 更新种群个体最优适应值
            min_index = np.unravel_index(np.argmin(self.best_fitness, axis=None), self.best_fitness.shape)   # 获取最小适应度位置
            self.gbest = self.pbest[min_index]  # 获得全局最优个体
            print(f"Best solution of {i+1}-th generation")
            print(self.gbest)

            # 画图需要
            global_best_fitness = np.amin(self.best_fitness)  # 当前最优适应值
            self.global_best_fitness_history.append(global_best_fitness)
            print(f"Best fitness of {i+1}-th generation: {global_best_fitness}:")
            print("Total Time:", time.time() - start)


start = time.time()
swarm = Swarm(50, 16)
swarm.swarm_init([0, 1])
print("Total Time:", time.time() - start)
swarm.train(0.9, 2, 2, 150)
print("Total Time:", time.time() - start)

plt.plot(swarm.global_best_fitness_history)
plt.xlabel("generation")
plt.ylabel("fitness")
plt.show()


