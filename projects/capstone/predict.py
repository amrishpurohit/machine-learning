#Read test data
sampleFile = pd.read_csv('data/sample_submission.csv')
sampleFile['parcelid'] = sampleFile['ParcelId']
sample = sampleFile.merge(prop, on='parcelid', how='left')
sample['New_transaction_month'] = train['New_transaction_month']

x_test = sample[train.columns]
