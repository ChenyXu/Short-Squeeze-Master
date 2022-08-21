import count
import fundingrates

asset = fundingrates.funding_rates()
data = count.Count(asset, [2022,8,15,0], [2022,8,21,0], 'short squeeze')

data_ = data.count()
print(data_)
