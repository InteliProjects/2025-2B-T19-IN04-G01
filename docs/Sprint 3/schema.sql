CREATE TABLE IF NOT EXISTS telemetry_professor (
    id BIGSERIAL PRIMARY KEY,
    pin VARCHAR(255) UNIQUE NOT NULL,
    model VARCHAR(255),
    modelo VARCHAR(255),
    stage VARCHAR(100),
    mdy INTEGER,
    spj INTEGER,
    cor VARCHAR(255),
    pais VARCHAR(255),
    m100 BIGINT,
    m200 BIGINT,
    m215 BIGINT,
    m244 BIGINT,
    m252 BIGINT,
    m282 BIGINT,
    m310 BIGINT,
    m313 BIGINT,
    g700 BIGINT,
    published_at BIGINT,
    scheduled_for BIGINT,
    original_stage_timestamp BIGINT,
    pr TEXT,
    received_at BIGINT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

ALTER TABLE telemetry_professor
    ADD COLUMN IF NOT EXISTS stage VARCHAR(100);

ALTER TABLE telemetry_professor
    ADD COLUMN IF NOT EXISTS published_at BIGINT;

ALTER TABLE telemetry_professor
    ADD COLUMN IF NOT EXISTS scheduled_for BIGINT;

ALTER TABLE telemetry_professor
    ADD COLUMN IF NOT EXISTS original_stage_timestamp BIGINT;

CREATE INDEX IF NOT EXISTS idx_telemetry_professor_pin ON telemetry_professor(pin);
CREATE INDEX IF NOT EXISTS idx_telemetry_professor_received_at ON telemetry_professor(received_at);
CREATE INDEX IF NOT EXISTS idx_telemetry_professor_model ON telemetry_professor(model);

COMMENT ON TABLE telemetry_professor IS 'Tabela de telemetria IoT - armazena dados brutos de sensores e dispositivos';
COMMENT ON COLUMN telemetry_professor.id IS 'Identificador único do registro (auto-incrementável)';
COMMENT ON COLUMN telemetry_professor.pin IS 'Código PIN do dispositivo/produto';
COMMENT ON COLUMN telemetry_professor.model IS 'Código do modelo';
COMMENT ON COLUMN telemetry_professor.modelo IS 'Descrição do modelo';
COMMENT ON COLUMN telemetry_professor.mdy IS 'Model Year (ano do modelo)';
COMMENT ON COLUMN telemetry_professor.spj IS 'Production Year (ano de produção)';
COMMENT ON COLUMN telemetry_professor.cor IS 'Código da cor';
COMMENT ON COLUMN telemetry_professor.pais IS 'Código do país';
COMMENT ON COLUMN telemetry_professor.m100 IS 'Timestamp Unix do estágio M100';
COMMENT ON COLUMN telemetry_professor.m200 IS 'Timestamp Unix do estágio M200';
COMMENT ON COLUMN telemetry_professor.m215 IS 'Timestamp Unix do estágio M215';
COMMENT ON COLUMN telemetry_professor.m244 IS 'Timestamp Unix do estágio M244';
COMMENT ON COLUMN telemetry_professor.m252 IS 'Timestamp Unix do estágio M252';
COMMENT ON COLUMN telemetry_professor.m282 IS 'Timestamp Unix do estágio M282';
COMMENT ON COLUMN telemetry_professor.m310 IS 'Timestamp Unix do estágio M310';
COMMENT ON COLUMN telemetry_professor.m313 IS 'Timestamp Unix do estágio M313';
COMMENT ON COLUMN telemetry_professor.g700 IS 'Timestamp Unix do estágio G700';
COMMENT ON COLUMN telemetry_professor.pr IS 'Parâmetros adicionais no formato CODE:VALUE separados por espaço';
COMMENT ON COLUMN telemetry_professor.received_at IS 'Timestamp Unix de quando o registro foi recebido pelo sistema';
COMMENT ON COLUMN telemetry_professor.created_at IS 'Timestamp de criação do registro no banco de dados';

CREATE TABLE IF NOT EXISTS wheel_hourly_summary (
    bucket_start TIMESTAMP WITH TIME ZONE NOT NULL,
    model_code VARCHAR(255) NOT NULL,
    rad_code VARCHAR(50) NOT NULL,
    wheel_description TEXT,
    cars_count INTEGER NOT NULL DEFAULT 0,
    wheels_count INTEGER NOT NULL DEFAULT 0,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    PRIMARY KEY (bucket_start, model_code, rad_code)
);

CREATE INDEX IF NOT EXISTS idx_wheel_summary_model ON wheel_hourly_summary(model_code);
CREATE INDEX IF NOT EXISTS idx_wheel_summary_bucket ON wheel_hourly_summary(bucket_start);

CREATE TABLE IF NOT EXISTS wheel_hourly_matrix (
    bucket_start TIMESTAMP WITH TIME ZONE PRIMARY KEY,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_wheel_matrix_bucket ON wheel_hourly_matrix(bucket_start);