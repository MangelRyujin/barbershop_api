from fastapi import HTTPException,status

def validate_phone(reservation_data):
    if not reservation_data.phone_number.isdigit() or not (900000000 <= int(reservation_data.phone_number) <= 999999999):
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Número de teléfono invalido"
            )  
