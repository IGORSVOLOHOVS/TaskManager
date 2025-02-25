// benches/benches-module1.rs
#[macro_use]
extern crate criterion;
use criterion::Criterion;

use my_project::modules::module1;


fn bench_function(c: &mut Criterion) {
	c.bench_function("module1::greet", |b| b.iter(|| module1::greet()));
}

criterion_group!(benches, bench_function);
criterion_main!(benches);