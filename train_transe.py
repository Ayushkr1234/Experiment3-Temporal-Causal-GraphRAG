from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline

# Load triples
tf = TriplesFactory.from_path("triples.tsv")

# Split into train and test
training, testing = tf.split([0.8, 0.2])

# Train TransE
result = pipeline(
    training=training,
    testing=testing,
    model="TransE",
    training_kwargs=dict(
        num_epochs=20
    )
)

# Save model
result.save_to_directory("transe_model")

print("TransE Training Complete")