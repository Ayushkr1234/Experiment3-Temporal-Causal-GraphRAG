from pykeen.pipeline import pipeline
from pykeen.triples import TriplesFactory

tf = TriplesFactory.from_path("triples.tsv")

training, testing = tf.split([0.8, 0.2])

result = pipeline(
    training=training,
    testing=testing,
    model="TransE",
    training_kwargs=dict(
    num_epochs=100
)
)

print("\n=== Metrics ===")

metrics = result.metric_results.to_dict()

print(metrics)