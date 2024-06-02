CREATE OR REPLACE FUNCTION trigger_calcular_dia_corte() 
RETURNS TRIGGER AS $$
BEGIN
    -- Llama al procedimiento que calcula y actualiza el dia de corte
    PERFORM calcular_dia_corte(NEW.ID_INQUILINO, NEW.ID_DEPARTAMENTO);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER trg_calcular_dia_corte
AFTER INSERT ON ARRIENDO
FOR EACH ROW
EXECUTE FUNCTION trigger_calcular_dia_corte();
