create table users(
	id_user int not null , 
	first_name varchar(255), 
	last_name varchar(255),
	result_covid bool not null, 
	registration_date date not null,
	test_date date not null, 
	result_date date,
    primary key (id_user));

create table personal_info(
	id_user int,
	age int,
	sex varchar(255),
	pre_diseases varchar(255),
	bmi int,
	fitness_level int,
	foreign key (id_user) references users(id_user),
	check (fitness_level between 1 and 10)
	
);

create table symptoms(
	id_user int,
	days_since_registration int,
	temperature decimal,
	taste int,
	pain int,
	smell int,
	foreign key (id_user) references users(id_user),
	check (taste between 1 and 10),
	check (smell between 1 and 10),
	check (pain between 1 and 10),
	check (temperature between 30 and 45)
	
);
