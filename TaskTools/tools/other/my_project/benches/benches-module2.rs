// benches/benches-module1.rs
#[macro_use]
extern crate criterion;
use criterion::Criterion;

use my_project::modules::module2;


fn bench_function(c: &mut Criterion) {
	c.bench_function("module2::greet", |b| b.iter(|| module2::greet()));
}

criterion_group!(benches, bench_function);
criterion_main!(benches);