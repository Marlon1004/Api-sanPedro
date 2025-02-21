CREATE DATABASE IF NOT EXISTS inscripcion_hospital;
USE inscripcion_hospital;

-- Tabla de Universidades
CREATE TABLE universidades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo_contacto VARCHAR(255) UNIQUE NOT NULL,
    datos_administrativos TEXT NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

-- Tabla de Estudiantes
CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    universidad_id INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    correo VARCHAR(255) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    carrera VARCHAR(255) NOT NULL,
    semestre INT NOT NULL,
    FOREIGN KEY (universidad_id) REFERENCES universidades(id) ON DELETE CASCADE
);

-- Tabla de Solicitudes
CREATE TABLE solicitudes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    universidad_id INT NOT NULL,
    fecha_solicitud TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('pendiente', 'aceptada', 'rechazada') DEFAULT 'pendiente',
    FOREIGN KEY (universidad_id) REFERENCES universidades(id) ON DELETE CASCADE
);

-- Tabla intermedia entre solicitudes y estudiantes
CREATE TABLE solicitud_estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    solicitud_id INT NOT NULL,
    estudiante_id INT NOT NULL,
    FOREIGN KEY (solicitud_id) REFERENCES solicitudes(id) ON DELETE CASCADE,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id) ON DELETE CASCADE
);

-- Tabla de Hospitales
CREATE TABLE hospitales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    correo_contacto VARCHAR(255) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

-- Tabla de Respuestas del Hospital a las solicitudes
CREATE TABLE respuestas_hospital (
    id INT AUTO_INCREMENT PRIMARY KEY,
    solicitud_id INT NOT NULL,
    hospital_id INT NOT NULL,
    estado ENUM('aceptada', 'rechazada') NOT NULL,
    fecha_respuesta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (solicitud_id) REFERENCES solicitudes(id) ON DELETE CASCADE,
    FOREIGN KEY (hospital_id) REFERENCES hospitales(id) ON DELETE CASCADE
);
