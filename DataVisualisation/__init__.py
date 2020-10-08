from DataVisualisation.task1 import data_visualization


def runVisualzation(K, dynamic_datasets_path):
    data_visualization(K, dynamic_datasets_path)


if __name__ == '__main__':
    K = 5
    dynamic_datasets_path = '..'
    runVisualzation(K, dynamic_datasets_path)
    exit()
