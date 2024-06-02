CREATE OR REPLACE FUNCTION calcular_dia_corte(p_id_inquilino INT, p_id_departamento INT) 
RETURNS VOID AS $$
DECLARE
    v_fecha_inicio DATE;
    v_dia_corte INT;
BEGIN
    -- Obtener la fecha de inicio para el arriendo dado
    SELECT FECHA_INICIO INTO v_fecha_inicio
    FROM ARRIENDO
    WHERE ID_INQUILINO = p_id_inquilino AND ID_DEPARTAMENTO = p_id_departamento;
    
    -- Verificar si se encontró el registro
    IF v_fecha_inicio IS NOT NULL THEN
        -- Calcular el día de corte basándose en el día de la fecha de inicio
        v_dia_corte := EXTRACT(DAY FROM v_fecha_inicio);
        
        -- Actualizar el día de corte en la tabla ARRIENDO
        UPDATE ARRIENDO
        SET DIA_CORTE = v_dia_corte
        WHERE ID_INQUILINO = p_id_inquilino AND ID_DEPARTAMENTO = p_id_departamento;
    ELSE
        RAISE NOTICE 'No se encontró arriendo con ID_INQUILINO = % y ID_DEPARTAMENTO = %', p_id_inquilino, p_id_departamento;
    END IF;
END;
$$ LANGUAGE plpgsql;
