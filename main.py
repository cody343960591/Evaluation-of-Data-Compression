import read_config
import sys
sys.path.append('./Algorithms')
import algo_select

if __name__ == "__main__":
    config = read_config.getConfig()
    algo_select.algo(**config)
    