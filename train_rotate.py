from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline

tf = TriplesFactory.from_path("triples.tsv")

training, testing = tf.split([0.8, 0.2])

result = pipeline(
    training=training,
    testing=testing,
    model="RotatE",
    training_kwargs=dict(
        num_epochs=20
    )
)

result.save_to_directory("rotate_model")

print("RotatE Training Complete")