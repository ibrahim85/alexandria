from sklearn.datasets import load_iris, load_diabetes

from alexandria.experiment import Experiment

if __name__ == '__main__':
	# Data preprocessing
	print('With sklearn.Bunch object...')
	iris = load_iris()

	experiment = Experiment(
		name='Cross Validation Example #1',
		dataset=iris,
		xlabels='data',
		ylabels='target',
		models=['rf', 'dt']
	)
	experiment.trainCV(nfolds=10, metrics=['accuracy', 'rec', 'prec'])
	experiment.summarizeMetrics()

	# Data preprocessing for dataframe object
	print('With pandas.DataFrame object...')
	diabetes_df = load_diabetes(as_frame=True).frame
	data_cols = diabetes_df.columns[:-1] # All columns, but the last one is the target
	target_col = diabetes_df.columns[-1] # 'target'

	experiment = Experiment(
		name='Cross Validation Example #2',
		dataset=diabetes_df,
		xlabels=data_cols,
		ylabels=target_col,
		models=['rf', 'dt']
	)
	experiment.trainCV(nfolds=10, metrics='r2')
	experiment.summarizeMetrics()