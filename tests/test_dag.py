import unittest
import pandas as pd
from unittest.mock import MagicMock
from Airflow.dags.src.data_prep import data_overview, data_validation, data_cleaning
from Airflow.dags.src.one_hot_encoder import encode_data
from Airflow.dags.data_prep_dag import (
    data_overview_callable,
    data_validation_callable,
    data_cleaning_callable,
    encode_data_callable,
)
from airflow.models import TaskInstance


class TestDagTasks(unittest.TestCase):

    def setUp(self):
        # Load real data for standard tests
        self.real_data = pd.read_csv('Methodology/AmesHousing.csv').head(5).to_json()

        # Edge case: Dataset with missing and extreme values
        self.anomalous_data = pd.DataFrame({
            'Gr Liv Area': [5000, 1000, 800, None, 3000],
            'Garage Yr Blt': [2207, 2007, None, 2000, 2005],
            'Lot Frontage': [70, None, 50, 100, None],
            'Mas Vnr Area': [None, None, None, None, None],
            'Bsmt Full Bath': [None, 1, None, 0, 2],
            'Bsmt Half Bath': [None, 0, None, None, 1],
            'BsmtFin SF 1': [None, 500, 800, None, 0],
            'Garage Cars': [2, None, 1, 3, None],
            'Electrical': [None, 'SBrkr', 'FuseA', None, 'SBrkr'],
            'Total Bsmt SF': [None, 1000, 800, 0, None],
            'Bsmt Unf SF': [None, 500, 300, None, 0],
            'BsmtFin SF 2': [None, 200, 0, None, 100],
            'Garage Area': [500, 400, None, 300, None],
            'Garage Cond': [None, 'TA', None, None, 'Gd'],
            'Garage Finish': [None, 'Unf', 'Fin', None, 'RFn'],
            'Garage Qual': [None, 'TA', None, None, 'Gd'],
            'Bsmt Exposure': [None, 'Gd', 'No', None, 'Av'],
            'BsmtFin Type 2': [None, 'ALQ', 'Unf', None, 'BLQ'],
            'Bsmt Qual': [None, 'Ex', 'TA', None, 'Gd'],
            'Bsmt Cond': [None, 'Gd', 'TA', None, 'Fa'],
            'BsmtFin Type 1': [None, 'GLQ', 'ALQ', None, 'Rec'],
            'Pool QC': [None, None, None, None, 'Ex'],  
            'Misc Feature': [None, 'Shed', None, None, None], 
            'Alley': [None, 'Grvl', None, None, 'Pave'], 
            'Fence': [None, 'MnPrv', None, None, None],
            'Garage Type': [None, 'Attchd', None, None, 'Detchd'], 
            'Fireplace Qu': [None, 'Gd', None, None, 'TA'], 
            'Mas Vnr Type': [None, 'Stone', None, None, 'None'],
        }).to_json()

    def test_data_overview_task(self):
        ti_mock = MagicMock(spec=TaskInstance)
        ti_mock.xcom_pull.return_value = self.real_data
        kwargs = {'ti': ti_mock}
        data_overview_callable(**kwargs)
        ti_mock.xcom_push.assert_called_once()

    def test_data_validation_task(self):
        ti_mock = MagicMock(spec=TaskInstance)
        ti_mock.xcom_pull.return_value = self.real_data
        kwargs = {'ti': ti_mock}
        data_validation_callable(**kwargs)
        ti_mock.xcom_push.assert_called_once()

    def test_data_cleaning_task(self):
        ti_mock = MagicMock(spec=TaskInstance)
        ti_mock.xcom_pull.return_value = self.real_data
        kwargs = {'ti': ti_mock}
        data_cleaning_callable(**kwargs)
        ti_mock.xcom_push.assert_called_once()

    def test_encode_data_task(self):
        ti_mock = MagicMock(spec=TaskInstance)
        ti_mock.xcom_pull.return_value = self.real_data
        kwargs = {'ti': ti_mock}
        encode_data_callable(**kwargs)
        ti_mock.xcom_push.assert_any_call(key='encoded_result', value=unittest.mock.ANY)

    def test_data_cleaning_with_anomalies(self):
        cleaned_data = data_cleaning(self.anomalous_data)
        cleaned_df = pd.read_json(cleaned_data)

        # Validate missing values were filled correctly
        self.assertNotIn(None, cleaned_df['Lot Frontage'].tolist())
        self.assertNotIn(None, cleaned_df['Mas Vnr Area'].tolist())
        self.assertNotIn(None, cleaned_df['Bsmt Full Bath'].tolist())
        self.assertNotIn(None, cleaned_df['Bsmt Half Bath'].tolist())
        self.assertNotIn(None, cleaned_df['BsmtFin SF 1'].tolist())
        self.assertNotIn(None, cleaned_df['Garage Cars'].tolist())
        self.assertNotIn(None, cleaned_df['Electrical'].tolist())
        self.assertNotIn(None, cleaned_df['Total Bsmt SF'].tolist())
        self.assertNotIn(None, cleaned_df['Bsmt Unf SF'].tolist())
        self.assertNotIn(None, cleaned_df['BsmtFin SF 2'].tolist())
        self.assertNotIn(None, cleaned_df['Garage Area'].tolist())
        self.assertNotIn(None, cleaned_df['Garage Yr Blt'].tolist())

        # Validate specific fill values
        self.assertEqual(cleaned_df['Mas Vnr Area'].min(), 1)  # Filled with 1
        self.assertEqual(cleaned_df['Bsmt Full Bath'].min(), 0)  # Filled with 0
        self.assertEqual(cleaned_df['Garage Yr Blt'].min(), 0)  # Filled with 0

    def test_data_cleaning_task_edge_cases(self):
        ti_mock = MagicMock(spec=TaskInstance)
        ti_mock.xcom_pull.return_value = self.anomalous_data
        kwargs = {'ti': ti_mock}
        data_cleaning_callable(**kwargs)
        ti_mock.xcom_push.assert_called_once()


if __name__ == '__main__':
    unittest.main()
