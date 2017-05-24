"""Base for categories."""

from model_utils import Choices


STATUS = Choices('active', 'inactive')
FREQUENCY = Choices(
    '5min',
    '10min',
    '20min',
    '30min',
    'weekly',
    'monthly',
    'daily',
    'forthnightly',
    'hourly'
)

freq_dic = {
    '5min': 0.083,
    '10min': 0.17,
    '20min': 0.33,
    '30min': 0.5,
    'hourly': 1,
    'daily': 24,
    'weekly': 168,
    'fornightly': 336,
    'monthly': 672
}
