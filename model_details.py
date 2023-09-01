import matplotlib.pyplot as plt
import seaborn as sns

"""
Helper methods to inspect model architecture and visualise metrics.
"""   
def plot_metrics(t_metric, v_metric, metric):
    """
    Displays accuracy and validation metrics plotted on line graphs.

    Args:
        t_metric (list): Accuracy/loss values during training.
        v_metric (list): Accuracy/loss values during validation.
        metric (str): Type of metric being plotted
    """
    sns.set(style='whitegrid')
    plt.figure(figsize=(10,6))
    plt.plot(t_metric, c='blue', label='Training', marker='x')
    plt.plot(v_metric, c='red', label='Validation', marker='o')
    plt.ylabel(f'{metric.title()}')
    plt.xlabel('Epoch')
    plt.title(f'Average {metric.title()}')
    plt.xticks(range(0, len(t_metric)), [
        str(i+1) for i in range(len(t_metric))
        ])
    plt.legend()
    plt.show()

def print_model_details(model, architecture=False, param_list=False):
    """
    Displays number of trainable weights and biases.
    Optionally display model architecture and list parameter values.

    Args:
        model (nn.Module): Model being inspected.
        architecture (bool, optional): Display model architecture.
            (default=False)
        param_list (bool, optional): Display trainable parameter
            values. (default=False).
    """
    # How many total trainable parameters there are
    num_params = sum(p.numel() for p in model.parameters())
    # Number of weights
    num_weights = sum(
        p.numel() 
        for p in model.parameters() 
        if p.requires_grad and len(p.shape) > 1
        )
    # Number of biases
    num_biases = sum(
        p.numel() 
        for p in model.parameters() 
        if p.requires_grad and len(p.shape) == 1
        )
    if architecture:
        print(model, '\n')


    print("{:,} weights.".format(num_weights))
    print("{:,} biases.".format(num_biases))
    print("{:,} total parameters.".format(num_params))
    if param_list:
        params = [
            (str(name), param.data) 
            for name, param in model.named_parameters()
            ]
        for param in params:
            print('\n', param[0])
            print(param[1])

def num_params(model):
    return sum(p.numel() for p in model.parameters())