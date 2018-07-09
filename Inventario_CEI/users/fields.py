from django.forms import CharField
from django.core.exceptions import ValidationError
from re import sub, match

class RutField(CharField):
  def validate(self, value):
    # Check the rut is valid.
    line = sub('[\\.-]', '', value)

    if not match("[0-9kK]*", line):
      raise ValidationError("Rut contiene carácteres no válidos.")

    counter = 2
    sum = 0
    for char in reversed(line[:-1]):
      sum += int(char) * counter
      counter = (counter - 1) % 6 + 2

    verifier = 11 - (sum % 11)

    if not (verifier==11 and line[-1]=="0" or
            verifier==10 and line[-1]=="k" or
            verifier==int(line[-1])):
      raise ValidationError("Rut no es válido.")

  def clean(self, value):
    super(RutField, self).clean(value)
    return sub('[\\.-]', '', value)


