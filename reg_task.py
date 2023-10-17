from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import pyspark.sql.types as t
import requests
url_pedagogai = "https://data.gov.lt/dataset/12/download/4468/Pedagogu%20kvalifikacija-12-lt-lt.csv"
spark = SparkSession.builder.appName("Read CSV from URL").getOrCreate()
def csv_to_df(spark, url, delimiter="\t"):
    data = requests.get(url)
    rdd = spark.sparkContext.parallelize(data.iter_lines())
    # Use the first row as the header
    header = rdd.first()
    rdd = rdd.filter(lambda line: line != header)
    # Create the PySpark DataFrame
    df = spark.createDataFrame(rdd.map(lambda line: line.decode("utf-8").split(delimiter)), header.decode("utf-8").split(delimiter))
    return df
df_pedagogai = csv_to_df(spark, url_pedagogai, "\t")
df_pedagogai = df_pedagogai.replace('','Nenurodyta')
for col in df_pedagogai.columns :
  text = ""
  for i in col :
    if i ==" " :
      text += "_"
    else :
      text += i
  df_pedagogai = df_pedagogai.withColumnRenamed(col, text.lower())
df_pedagogai = df_pedagogai \
    .withColumn("pd_institucijos_savivaldybės_id", F.col("pd_institucijos_savivaldybės_id").cast(t.IntegerType())) \
    .withColumn("pd_pareigų_grupė_id", F.col("pd_pareigų_grupė_id").cast(t.IntegerType())) \
    .withColumn("pd_pedagogų_skaičius", F.col("pd_pedagogų_skaičius").cast(t.IntegerType()))
df_transf=df_pedagogai\
  .select('pd_institucijos_savivaldybė','pd_pedagogų_skaičius')\
  .where(F.col('pd_pareigų_grupė') == "Mokytojai")\
  .groupBy('pd_institucijos_savivaldybė')
df_transf.sort('pd_institucijos_savivaldybė').show()
df_transf.orderBy('pd_institucijos_savivaldybė', ascending = True).show()
from pyspark.sql.functions import sum, when
df_pedagogai.select(sum(when(F.col('pd_pareigų_grupė') == "Mokytojai", F.col('pd_pedagogų_skaičius')))).show()