import DataVisualisation
import NearestNeighbors

if __name__ == '__main__':
    K = 5
    dynamic_datasets_path = ''

    DataVisualisation.runVisualzation(K, dynamic_datasets_path)

    NearestNeighbors.runA1andA2(K, dynamic_datasets_path)

    exit()
