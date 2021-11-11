import pandas as pd
from typing import List, Dict

from rexmex.utils import binarize

from scipy.stats.stats import pearsonr
from sklearn.metrics import roc_auc_score
from sklearn.metrics import f1_score, precision_score, recall_score, average_precision_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score

from rexmex.metrics import pr_auc_score
from rexmex.metrics import symmetric_mean_absolute_percentage_error, root_mean_squared_error

class MetricSet(dict):
    """
    """   
    def _get_metrics(self, filter: List[str]=None) -> Dict:
        """
        """
        if filter is None:
            selected_metrics = self
        else:
            selected_metrics = {name: metric for name, metric in self.items()}
        return selected_metrics
    
    def get_performance_metrics(self, y_true, y_score, filter: List[str]=None) -> pd.DataFrame:
        """
        """
        selected_metrics = self._get_metrics(filter)
        performance_metrics = {name: [metric(y_true, y_score)] for name, metric in selected_metrics.items()}
        performance_metrics = pd.DataFrame.from_dict(performance_metrics)
        return performance_metrics

    def filter_metric_set(self, filter: List[str]=None):
        for name, _ in self.items():
            del self[name]

class ClassificationMetricSet(MetricSet):
    """
    """
    def __init__(self):
        self["roc_auc"] = roc_auc_score
        self["pr_auc"] = pr_auc_score
        self["average_precision"] = average_precision_score
        self["f1_score"] = binarize(f1_score)
        self["precision"] = binarize(precision_score)
        self["recall"] = binarize(recall_score)

class RatingMetricSet(MetricSet):
    """
    """
    def __init__(self):
        self["mae"] = mean_absolute_error
        self["mse"] = mean_squared_error
        self["rmse"] = root_mean_squared_error
        self["mape"] = mean_absolute_percentage_error
        self["smape"] = symmetric_mean_absolute_percentage_error
        self["r_squared"] = r2_score
        self["pearson_correlation"] = pearsonr

class CoverageMetricSet(MetricSet):
    """
    """
    def setup_basic_metrics(self):
        pass

class RankingMetricSet(MetricSet):
    """
    """
    def setup_basic_metrics(self):
        pass